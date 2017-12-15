def f(v):
    if v % 2 == 0:
        v = v ** 2
    else:
        v = v + 1
    return v


result = [f(v) for v in [2, 3, 4, -1] if v > 0]
print(result)
print("=" * 10)
result2 = [v ** 2 if v % 2 == 0 else v + 1 for v in [2, 3, 4, -1] if v > 0]
print(result2)
