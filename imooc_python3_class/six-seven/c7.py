''' for target_list in range(10, 0, -2):
    print(target_list, end=" | ")
'''

a = [1, 2, 3, 4, 5, 6, 7, 8]
''' 
for x in range(0, len(a), 2):
    print(a[x], end=" | ") '''
b = a[0:len(a):2]
print(b)