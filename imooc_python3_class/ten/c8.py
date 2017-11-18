import re

a = "PythonC++JAVA\n45PHP\n45"
# [] -> ||
# () -> &&
r = re.findall("php.{1}", a, re.I | re.S)
print(r)
