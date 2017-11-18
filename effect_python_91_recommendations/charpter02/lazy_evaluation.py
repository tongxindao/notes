from time import time

t = time()
abbreviations = ["cf.", "e.g.", "ex.", "etc.", "fig.", "i.e.", "Mr.", "vs."]

for i in range(1000000):
    for w in ("Mr.", "Hat", "is", "chasing", "the", "black", "cat", "."):
        # if w in abbreviations:
        if w[-1] == "." and w in abbreviations:
            pass

print("total run time:")
print(time()-t)
