import re

a = "Python\nC++\nPHP\nJAVA\nPHP"

def convert(value):
    matched = value.group()
    return "!!" + matched + "!!"

# r = re.sub("php", "GO", a, 1, re.I)
r = re.sub("php", convert, a, 0, re.I)
print(r)
