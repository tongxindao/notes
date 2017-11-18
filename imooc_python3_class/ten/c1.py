import re

a = "C|C++|JAVA|Python|Javascript"

r = re.findall("PHP", a)
if len(r) > 0:
    print("String include string 'PHP'")
else:
    print("No matches string.")
    
# print(r)

# print(a.index("Python") > -1)
# print("Python" in a)