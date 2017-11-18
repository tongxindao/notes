import re

a = "ABC3721086"

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
         return '0'

r = re.sub("\d", convert, a)
print(r)
