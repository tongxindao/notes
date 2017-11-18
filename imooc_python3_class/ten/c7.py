import re

a = "PythonPythonPythonPython"
# [] -> ||
# () -> &&
r = re.findall("{Python}{1}", a)
print(r)
