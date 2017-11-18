import re

qq = "10010318"

r = re.findall("^\d{4,8}$", qq)
print(r)
