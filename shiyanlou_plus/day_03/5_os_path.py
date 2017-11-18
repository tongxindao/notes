import os

filename = "/home/shiyanlou/Code/shiyanlou/shiyanlou_plus/day_03/test.txt"

print(os.path.abspath(filename))
print(os.path.basename(filename))
print(os.path.dirname(filename))
print(os.path.isfile(filename))
print(os.path.isdir(filename))
print(os.path.exists(filename))
print(
    os.path.join(
        "/home/shiyanlou/Code/shiyanlou/shiyanlou_plus/day_03",
        "test.txt"))
