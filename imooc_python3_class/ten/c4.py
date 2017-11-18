import re
# \d
# \w
# \s

a = "python\t\r1111java&_67\n8 php"

r = re.findall("\W", a)
print(r)
