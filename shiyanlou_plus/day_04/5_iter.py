letters = ['a', 'b', 'c']

for letter in letters:
    print(letter)

print("=" * 30)

it = iter(letters)
try:
    for i in range(4):
        print(next(it))
        i += 1
except:
    print("StopIteration")

print("=" * 30)

it = letters.__iter__()
try:
    for i in range(4):
        print(it.__next__())
        i += 1
except:
    print("StopIteration")

"""
    能被for循环访问的都是可迭代的对象，能被next()函数获取下一值的是迭代器。
"""
