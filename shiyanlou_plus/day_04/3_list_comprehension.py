numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = [x for x in numbers if x % 2 == 0]
print(x)

y = [y * y for y in numbers]
print(y)

# filter(function or None, iterable) --> filter object
f = filter(lambda x: x % 2 == 0, numbers)
print(list(f))

# map(func, *iterables) --> map object
m = map(lambda x: x * x, numbers)
print(list(m))
