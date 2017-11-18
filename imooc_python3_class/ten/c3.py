import re

a = "abc, acc, adc, aec, afc, ahc"

r = re.findall("a[c-f]c", a)
print(r)
