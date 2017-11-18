import re
# \d
# \w
# \s

a = "pytho01111python678pythonn2"

r = re.findall("python{1,2}?", a)
print(r)
