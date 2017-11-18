import re

s = "Life is short, i use python, i use python"

r = re.search("Life(.*)python(.*)", s)
# print(r.group(0, 1, 2))
print(r.groups())
# r = re.findall("Life(.*)python", s)
# print(r)