# list_x = [1, 0, 1, 0, 1, 0, 1]
# r = filter(lambda x: True if x == 1 else False, list_x)
# r = filter(lambda x: x, list_x)
# print(list(r))

list_u = ["A", "b", "c", "D", "e", "F"]
print(list(filter(lambda x: ord(x) >= 97, list_u)))