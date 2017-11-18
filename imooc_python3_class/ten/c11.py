import re

s = "1AB3C72D1DBE67"

r = re.match("\d", s)
print(r.span())
r1 = re.search("\d", s)
print(r1.group())
r2 = re.findall("\d", s)
print(r2)