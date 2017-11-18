import re

a = "C7C++8JAVA9Python10Javascript"

r = re.findall("\D", a)
print(r)
# if len(r) > 0:
#     print("String include string 'PHP'")
# else:
#     print("No matches string.")
