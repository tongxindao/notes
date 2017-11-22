import json
from collections import OrderedDict

d = OrderedDict()
d["apple"] = 1
d["google"] = 2
d["facebook"] = 3
d["amazon"] = 4

for key in d:
    print(key, d[key])

print(json.dumps(d))
