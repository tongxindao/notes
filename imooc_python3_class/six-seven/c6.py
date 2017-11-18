expression_list = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]

for x in expression_list:
    if 'banana' in x:
        break
    for y in x: 
        if y == 'orange':
            break
        print(y)
else:
    print("It's gone!")

''' 
a = [1, 2, 3]

for x in a:
    if x == 2:
        # break
        continue
    print(x)
else:
    print("EOF")
     '''